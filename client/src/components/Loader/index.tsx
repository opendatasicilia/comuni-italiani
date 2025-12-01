interface ILoader {
  className?: string;
}

export const Loader = ({ className }: ILoader) => {
  const baseClass = "d-flex justify-content-center align-items-center";
  return (
    <div className={`${baseClass} ${className}`}>
      <div className="spinner-border" role="status">
        <span className="visually-hidden">Loading...</span>
      </div>
    </div>
  );
};
